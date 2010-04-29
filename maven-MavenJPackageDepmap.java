package org.apache.maven.artifact.repository.layout;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;
import org.xml.sax.InputSource;

public class MavenJPackageDepmap {

	private static  MavenJPackageDepmap instance;
	private static Hashtable jppArtifactMap;

	private MavenJPackageDepmap() {
		jppArtifactMap = new Hashtable();
		buildJppArtifactMap();
	}
	
	public static MavenJPackageDepmap getInstance() {
		if (instance == null) {
			instance = new MavenJPackageDepmap();
		}
		
		return instance;
	}

	public Hashtable getMappedInfo(Hashtable mavenDep) {
		return getMappedInfo((String) mavenDep.get("group"), 
							(String) mavenDep.get("artifact"), 
							(String) mavenDep.get("version"));
	}

	public Hashtable getMappedInfo(String groupId, String artifactId, String version) {

		Hashtable jppDep;
		String idToCheck, jppCombination;

		if (System.getProperty("maven2.ignore.versions") == null && System.getProperty("maven2.jpp.mode") == null) {
			idToCheck = groupId+","+artifactId+","+version;
		} else {
			idToCheck = groupId+","+artifactId;
		}

		jppCombination = (String) jppArtifactMap.get(idToCheck);

		//System.err.println("*** " + groupId+","+artifactId+","+version + " => " + jppCombination);
		
		jppDep = new Hashtable();
		if (jppCombination != null && jppCombination != "") {

			StringTokenizer st = new StringTokenizer(jppCombination, ",");

			jppDep.put("group", st.nextToken());
			jppDep.put("artifact",st.nextToken());
			jppDep.put("version",st.nextToken());

		} else {
			jppDep.put("group", groupId);
			jppDep.put("artifact", artifactId);
			jppDep.put("version", version);
		}

		return jppDep;
	}


	/**
	 *	Returns whether or not the given dependency should be dropped.
	 */
	public boolean shouldEliminate(String groupId, String artifactId, String version) {
		String idToCheck;

		if (System.getProperty("maven2.ignore.versions") == null && System.getProperty("maven2.jpp.mode") == null) {
			idToCheck = groupId+","+artifactId+","+version;
		} else {
			idToCheck = groupId+","+artifactId;
		}

		return jppArtifactMap.get(idToCheck) != null && jppArtifactMap.get(idToCheck).equals("");

	}

	private static void buildJppArtifactMap() {

		if (System.getProperty("maven2.ignore.versions") != null || System.getProperty("maven2.jpp.mode") != null) {
			//System.err.println("Processing file: /usr/share/java-utils/xml/maven2-versionless-depmap.xml");
			processDepmapFile("/etc/maven/maven2-versionless-depmap.xml");
		}

		//System.err.println("Processing file: /usr/share/java-utils/xml/maven2-depmap.xml");
		processDepmapFile("/etc/maven/maven2-depmap.xml");

		String customFileName = System.getProperty("maven2.jpp.depmap.file", null); 
		if (customFileName != null) {
			//System.err.println("Processing file: " + customFileName);
			processDepmapFile(customFileName);
		}
	}

	private static void processDepmapFile(String fileName) {
		
		Document mapDocument;

		try {
			mapDocument = (new SAXBuilder()).build(new InputSource(new FileInputStream(fileName)));
		} catch (FileNotFoundException fnfe) {
			System.err.println("ERROR: Unable to find map file: " + fileName);
			fnfe.printStackTrace();
			return;
		} catch (IOException ioe) {
			System.err.println("ERROR: I/O exception occured when opening map file");
			ioe.printStackTrace();
			return;
		} catch (JDOMException jde) {
			System.err.println("ERROR: Unable to instantiate parser");
			jde.printStackTrace();
			return;
		}
		
		List l = mapDocument.getRootElement().getChildren("dependency");
		
		Iterator i = l.iterator();
		while (i.hasNext()) {
			Element depElement = (Element) i.next();

			Element mElem = depElement.getChild("maven");
			Element jppElem = depElement.getChild("jpp");
			
			String mG = mElem.getChildText("groupId");
			String mA = mElem.getChildText("artifactId");
			String mV = mElem.getChildText("version");

			// jppElem == null => drop this dependency
			if (jppElem != null) {

				String jppG = jppElem.getChildText("groupId");
				String jppA = jppElem.getChildText("artifactId");
				String jppV = jppElem.getChildText("version");
                                jppV = jppV != null && jppV.length() > 0 ? jppV : mV;

				if (System.getProperty("maven2.ignore.versions") == null && System.getProperty("maven2.jpp.mode") == null) {
					//System.err.println("*** Adding: " + mG+","+mA+","+mV + " => " +  jppG+","+jppA+","+jppV + " to map...");
					jppArtifactMap.put(mG+","+mA+","+mV, jppG+","+jppA+","+jppV);
				} else {
					//System.err.println("*** Adding: " + mG+","+mA + " => " +  jppG+","+jppA+","+jppV + " to map...");
					jppArtifactMap.put(mG+","+mA, jppG+","+jppA+","+jppV);
				}
			} else {
					//System.err.println("*** Adding: " + mG+","+mA+"," + " => " +  "JPP/maven2,empty-dep,"+mV + " to map...");
					jppArtifactMap.put(mG+","+mA, "JPP/maven2,empty-dep,"+mV);
			}
		}
	}
}

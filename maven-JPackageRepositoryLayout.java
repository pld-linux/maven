package org.apache.maven.artifact.repository.layout;

/*
 * Copyright 2001-2005 The Apache Software Foundation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *	  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;

import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.handler.ArtifactHandler;
import org.apache.maven.artifact.metadata.ArtifactMetadata;
import org.apache.maven.artifact.repository.ArtifactRepository;
import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;
import org.xml.sax.InputSource;

/**
 * Repository layout for jpackage based repositories. 
 * This class resolves items for jpp style repos (i.e things located in 
 * /usr/share/java).
 */

public class JPackageRepositoryLayout
	implements ArtifactRepositoryLayout
{
	private static Hashtable jppArtifactMap;

	private static final char GROUP_SEPARATOR = '.';
	private static final char PATH_SEPARATOR = '/';

	public String pathOf( Artifact artifact )
	{

		ArtifactHandler artifactHandler = artifact.getArtifactHandler();
		StringBuffer path = new StringBuffer();

		String artifactId = artifact.getArtifactId();
		String groupId = artifact.getGroupId();
		String version = artifact.getVersion();
		String classifierSuffix = (artifact.getClassifier() == null || artifact.getClassifier() == "") ? 
		                          "" : "-" + artifact.getClassifier();

		if (!groupId.startsWith("JPP")) {
			MavenJPackageDepmap map = MavenJPackageDepmap.getInstance();
			Hashtable newInfo = map.getMappedInfo(groupId, artifactId, version);
			
			groupId = (String) newInfo.get("group");
			artifactId = (String) newInfo.get("artifact");
		}

		if (groupId.startsWith("JPP")) {
			if (artifactHandler.getPackaging().equals("pom")) {
				path = getPOMPath(groupId, artifactId);

			} else {    // Assume if it is not pom it is jar
                                    // as "maven-plugin" type is a JAR
				path.append( groupId ).append( '/' );
				path.append( artifactId ).append(classifierSuffix).append( "." + artifactHandler.getExtension());
			}
		} else {
			path.append( groupId.replace(GROUP_SEPARATOR, PATH_SEPARATOR) ).append( '/' ).append( artifactId ).append( '/' ).append( version ).append( '/' );
			path.append( artifactId ).append( '-' ).append( version ).append( "." );
                        // Parent poms may come with type "xml"
			if (artifactHandler.getPackaging().equals("xml")) {
				path.append( "pom" );
			} else {
				path.append( artifactHandler.getPackaging() );
			}
		}

		return path.toString();
	}

	private StringBuffer getPOMPath(String groupId, String artifactId) {

		StringBuffer path = new StringBuffer();
		String fName = groupId.replace(PATH_SEPARATOR, GROUP_SEPARATOR) + "-" + artifactId + ".pom";
		path.append(System.getProperty("maven2.jpp.pom.path", "JPP/maven2/poms")).append("/").append(fName);
		java.io.File f;

		// NOTE: We are returning default_poms/ as the path for this pom 
		// even though it may not exist there. This may cause an error, 
		// but that is fine because if the pom is not there, there is 
		// a serious problem anyways..
		f = new java.io.File(System.getProperty("maven2.jpp.default.repo", "/usr/share/maven2/repository") + "/" + path.toString());
		System.err.println("Checking path " + f.getAbsolutePath() + " for the pom");
		if (!f.exists()) {
            System.err.println(f.getAbsolutePath() + " not found");
			path = new StringBuffer();
			path.append(System.getProperty("maven2.jpp.default.pom.path", "JPP/maven2/default_poms")).append("/").append(fName);
		}

		return path;
	}

	public String pathOfLocalRepositoryMetadata( ArtifactMetadata metadata, ArtifactRepository repository )
	{
		return pathOfRepositoryMetadata( metadata, metadata.getLocalFilename( repository ) );
	}

	private String pathOfRepositoryMetadata( ArtifactMetadata metadata, String filename )
	{

        StringBuffer path = new StringBuffer();

        if (filename.substring(filename.length()-4).equals(".pom")) {
			path = getPOMPath(metadata.getGroupId(), metadata.getArtifactId());
        } else {

		// FIXME: If it gets here, something other than a pom was requested.. where are those things located?
		path.append(System.getProperty("maven2.jpp.pom.path", "maven2/poms")).append("/").append(filename);
        }

		return path.toString();
	}

	public String pathOfRemoteRepositoryMetadata( ArtifactMetadata metadata )
	{
		return pathOfRepositoryMetadata( metadata, metadata.getRemoteFilename() );
	}
}

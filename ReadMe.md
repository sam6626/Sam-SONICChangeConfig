#### ConfigReplace Overview

The Configuration Replacement and Rollback feature provides the capability to replace the current running configuration, i.e., CONFIG_DB, with a known good configuration file saved in the serialization of DB format, i.e. config_db.json. Currently SONiC utility "config reload" or Klish command "copy source-url running-configuration overwrite" is provided to replace configuration, but both methods require some core services restarted. This feature is designed to limit the impact to features/services that are being replaced, with minimum service disruption.

Config replace operation can be executed in either via exec CLI mode (config terminal) or the new session mode (config session). 

#### Config Replace in Session mode

 \-   Configure session mode has the below CLI options for performing the configuration replace on Dell Enterprise SONiC switch,

\-    Replace: New CLI introduced as part of config-replace feature, this command used to perform config replace from configure session mode.

\-    Commit timeout: Timer option added to commit command for user to apply the changes to CONFIG_DB on trial basis, if a timer gets expired, rollback to the previous configuration.

\-    Commit confirm: Confirm option added to commit command for user to confirm new configuration changes. (Move trial to permanent stage)

\-    Commit: Committing the new configuration changes.

Steps:

1. 

\-    Abort: When "clear config session" is executed from CLI – the commit timeout will be cancelled and rollback to previous running-configuration if “commit timeout” is configured. Or it just aborts the configurations from the session.

#### Config Replace in Exec mode

 Perform this operation to replace the current running configuration with a saved Dell Enterprise SONiC configuration file.

Note: User must create a configuration file in supported file format before performing this operation.

Steps:

1. copy *source-url* running-configuration replace

 

## Generating the configuration file

configuration file is generated by the copy running-configuration destination-url command or if generated externally, the configuration file must fulfil with the format of files generated by Dell Enterprise SONiC devices. Configuration files can be stored and available for use with the “copy source-url running-configuration replace” command, can be located on the following file systems:
-	config:  Copy from configuration directory (config://filename)
-	ftp:     Copy from remote FTP server (ftp://userid:passwd@hostip/filepath)
-	home:    Copy from home directory (home://filename)
-	http:    Copy from remote HTTP server (http://hostip/filepath)
-	scp:     Copy from remote SCP server (scp://userid:passwd@hostip/filepath)
-	usb:     Copy from usb media directory (usb://filename)

The copy source-url running-configuration replace command provides the capability to replace the current running configuration with any saved Dell Enterprise SONiC configuration file. Using this functionality, we can revert to a previous configuration state if previous configuration state is saved in config file.




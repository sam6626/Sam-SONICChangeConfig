#### Using PyGNOI to automate configuration change leveraging ConfigReplace

- Read this section if you want to explore using PyGNOI with copyconfig

- In case you are using to integrate Configreplace in your gPRC programmatic logic or code. Here is a quick sample command using the built-in gNOI client to trigger the Configreplace. 

- gNOI (gRPC Network Operations Interface) extends the gNMI server, adding new custom RPC's to execute management functions on the switch.

- SONiC NOS has an integrated built-in the SONiC repo as per this [link](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/Management%20Framework.md#3223-gnmi-client)

- The built in Gnoi client supports the below rpc Copy functionality through the Opencofig FileMgmt module

  Example 

  gnoi_client -module Openconfig FileMgmtPrivate -rpc Copy -jsonin '{"openconfig-file-mgmt-private:input":{"source":"config://config_db.json","destination":"running-configuration","copy-config-option":"REPLACE"}}' -insecure -username <user_name> -password <passwd>

  

  Note: gNMI not supported for config-replace.

-  For examples and command details please check the corresponding section in Dell Enterprise SONiC - ConfigReplace [Testing document here](https://github.com/sam6626/Sam-SONICChangeConfig/blob/main/Assests/ConfigReplace%20Prelauch%20test%20Sonic%204%201%20-%202.pdf)

- The above gnoi client used in the above work and testing is the integrated built-in the SONiC repo as per this [link](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/Management%20Framework.md#3223-gnmi-client)

- 

- Here is another example of using the built in Gnoi client to clear IP neighbors

  example 2

  gnoi_client -module Sonic -rpc clearNeighbors -jsonin '{"sonic-neighbor:input": {"force": true, "ip": "4.4.4.1"}}' -insecure

- gNOIc by [Karimra]() does not support copy configs .. yet it does come with a handy [pypi](https://pypi.org/project/gnoi-client/) ! 
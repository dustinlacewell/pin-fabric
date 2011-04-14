pin-fabric
=======

pin-fabric provides 'project-wide' access to commands inside your fabfile.py file. pin-fabric will list your fabric commands in the **pin help** command.

$ pin help
usage: pin [-v]

optional arguments:
  -v, --version  show program's version number and exit

Available commands for /home/dlacewell/dev/pmcs:
destroy  - Destroy and unregister the project from pin.
     go  - Teleport to a specific project.
   help  -  This help information. 
   init  - Initialize pin in the current directory.
    fab  --------------------------------------------------------------------------
         Commands inside your fabfile.
         update_remote  - Update deployment server and restart apache
            push_local  - Push locally commited changes

### Commands

* **pin fab [fabric args]** : Execute any commands inside your fabfile.py file

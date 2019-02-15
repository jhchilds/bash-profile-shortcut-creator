# bash_profile_shortcut_creator
A very small, but time saving python script that asks user for an alias name, and creates a shortcut with this alias in their .bash_profile to their present working directory.


## For Best Results 

### Create 2 shortcuts in your bash profile:
1. Running bash_write.py shortcut
```
sudo nano ~/.bash_profile
```
use the syntax:

```
alias [alias_name]='python3 [path_to_file]/bash_write.py $(pwd)'
```

2. Rendering .bash_profile

```
alias [alias_name]='source ~/.bash_profile'
```

I use the alias `   new   `, so that if I want to create a shortcut to a deep directory, I can simply navigate to it,
type in new, and this program will prompt for an alias name. Use the #2 shortcut above to confirm this recently created shortcut (if you don't do this, your shortcut will not be activated)

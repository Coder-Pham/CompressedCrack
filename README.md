# About the project
This tool is made to test my programming skill. You may found it quiet easy and interesting for you to code the same. But Hey, I code it just for fun.  
I'm still working on this project because it's not fully-equiped.   
I tend to change it from Python2 to Python3, because Python3 has more library working on Compressed, so maybe I can crack .rar or .tar files too.     

If you have any suggestion about this project, please tell me, maybe we can develop it together.   
# Prerequisites
To run this quickstart, you’ll need:

<ul>
<li> Python 2 or greater.    
<li> The pip package management tool.     
<li> A good knowlegde about Powershell or Bash.  
</ul>

# Usage
## General syntax:
```
python Zip.py -z <Zip File Name> 
```
`<Zip File Name>` where we type your zip file that need to cracked password.      

For example, I have a `test.zip` that need to cracked. I shall type:   
	```
	python Zip.py -z test.zip
	```

General help text:
```
Optional arguments:
	-h, --help				Show this help message and exit
	-z, ZIP					Zip file name
	-min	MIN				Minium length of the password (if you know)
	-max MAX				Maxium length of the password (if you know)
	-r RULE					The characters or number that will have in the password
```

## List optional arguments:
### -min MIN
```sh
python Zip.py -z <File Name> -min <Minium length> 
```

**>>** This command will make the cracking progress start at <Minium length>-length password.  
**>>** But if the password has the length smaller than <Minium length> value, the progess will run infinite.  
	
### -max MAX
```sh
python Zip.py -z <File Name> -max <Maxium length> 
```

**>>** This command will make the cracking progerss end at <Maxium length>-length password.  	
	
**>>** But if the password has the length greater than <Maxium length> value, the progess will throw error.  
	
### -r RULE
```sh
python Zip.py -z <File Name> -r <Characters>
```

**>>** This command will make the cracking progress generate password list base on RULE.

**>>** But if the password has characters outside the given rule, the progress will run infinite.

**NOTE that we can combine all optional arguments in order to cracking password faster.**

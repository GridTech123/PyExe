import cx_Freeze
import os
import sys

def build(pythonFile, name, version, modules, files):
    try:
        f = open(name +'_pyExe.py', 'w')
    except:
        try:
            print 'error: could not make file ' + name +'_pyExe.py'
        except:
            print 'there was an error making an error message'
    f.write('import cx_Freeze')
    f.write('\n')
    try:
        f.write('executables = [cx_Freeze.Executable("' +str(pythonFile)+'.py' +'")]')
    except:
        try:
            print 'we could not find ' +str(pythonFile) +'.py'
        except:
            print 'there was an error making an error message'
    f.write('\n')
    f.write('cx_Freeze.setup(name = "' +str(name) +'", version = "' +str(version) +'", options = {"build_exe": {"packages":' +str(modules) +' , "include_files":' +str(files) + '}}, executables = executables)')
    try:
        os.system(''+str(name) +'_pyExe.py build')
    except:
        print 'error: could not run file created'
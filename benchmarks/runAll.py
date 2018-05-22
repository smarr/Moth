import subprocess

configs = {

    "Richards" : {
        "outer" : 1000,
        "warmup" : 0,
        "inner" : 60
    },

    "Snake" : {
        "outer" : 1000,
        "warmup" : 0,
        "inner" : 50
    },

    "CallMany" : {
        "outer" : 1000,
        "warmup" : 0,
        "inner" : 50000
    },

    "Ackermann" : {
        "outer" : 1000,
        "warmup" : 0,
        "inner" : 100
    },

    "Splay" : {
        "outer" : 100,
        "warmup" : 0,
        "inner" : 10
    },

    "Raytrace" : {
        "outer" : 100,
        "warmup" : 0,
        "inner" : 10
    }

}

def exe():
    for key in configs.keys():
        name = key
        outer  = configs[key]["outer"]
        warmup = configs[key]["warmup"]
        inner  = configs[key]["inner"]
        command = "./benchmarks/compareUntypedAndTyped %s %d %d %d" % (name, outer, warmup, inner)
        subprocess.run(command.split(" "))
exe()
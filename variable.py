palette = { 
        "white":(255,255,255), 
        "black":(0,0,0), 
        "red":(255,0,0), 
        "green":(0,255,0), 
        "blue":(0,0,255), 
        "magenta":(255,0,255), 
        "orange":(255,127,0),
        "pink":(255,192,203), 
        "brown":(150,75,0), 
        "cyan":(0,255,255), 
        "indigo":(75,0,130), 
        "purple":(128,0,128), 
        "violet":(143,0,255), 
        "gray":(128,128,128) 
        }

if __name__ == "__main__":
    for key in sorted(palette.keys()):
        print(key, palette[key])

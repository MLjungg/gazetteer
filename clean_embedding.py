# Path to embed without extension (.txt).
PATH_TO_EMBED_FILE = "/Users/mikael/Documents/Programmeringsprojekt/coreNLP-Swedish/Dependency-Parser/embed/model_embed"

embed_file_read = open(PATH_TO_EMBED_FILE+".txt", "r")
embed_file_write = open(PATH_TO_EMBED_FILE + '_cleaned.txt', "w")

bad_words = ["-0.236309", "6", "2", "0.031622", "68", "0250", "97", "34706", "326296", "ost1/2", 'förening".', "176", ".091885", "33", "740", "0.026457", "4", "-0.150838", "idrottsföräldrarna", ".149971", "087886", "087886","117", "-0.228755", "087886", "-0.084290", "0.067463",".084847","1912–2012.", "16","93","36027",'', "0.117226","049965","00","0.011824","095515","168",".069699", "17"]

iter = 0
while iter < 3010197:
    try:
        for line in embed_file_read:
            iter += 1
            word = line.split(" ")[0]
            if word in bad_words:
                continue
            embed_file_write.write(line)
    except UnicodeDecodeError:
        iter += 1
        continue
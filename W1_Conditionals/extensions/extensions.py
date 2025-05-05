file = input("File name: ").strip().lower()

match file.split(".")[-1]: #split separates everything before and after dot. -1 selects last item in string list
    case "gif":            print("image/gif")
    case "jpg" | "jpeg":   print("image/jpeg")
    case "png":            print("image/png")
    case "pdf":            print("application/pdf")
    case "txt":            print("text/plain")
    case "zip":            print("application/zip")
    case _:                print("application/octet-stream")

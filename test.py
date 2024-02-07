from computer import Computer

def main():
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,"macOS Big Sur", 2013, 1500)
    
    print(computer1.operating_system)
    
    computer1.os_change("windows")
    print(computer1.operating_system)

    



















if __name__ == "__main__": main()

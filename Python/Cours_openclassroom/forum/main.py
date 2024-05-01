import package as pac


def main():
    pac.init_main()
    thread = pac.Shell.list_obj_user[1].add_thread()
    thread.display()

if __name__ == "__main__":
    main()

        
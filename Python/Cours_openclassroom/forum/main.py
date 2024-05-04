import package as pac


def main():
    pac.init_main()
    #thread = pac.Shell.list_obj_user[1].add_thread()
    pac.Shell.list_obj_thread[0].display()

    #post = pac.Post("coucou!!", pac.Shell.list_obj_user[1].name, date_in="Sat May  4 14:27:27 2024", id_='p8495')
    #print(post.__repr__()[0])
    #alice = pac.Admin("guix", "abab")

    #print(pac.Shell.list_posts)
    #print(pac.Shell.list_obj_user[1].name)

    
    

if __name__ == "__main__":
    main()

        
import package as pac


def main():
    pac.init_main()
    print(pac.Shell.list_user)
    print(pac.Shell.list_posts)
    print(pac.Shell.list_threads)
    #print(pac.Shell.list_obj_user[0].__repr__())
    #print(pac.Shell.list_obj_post[0].__repr__())
    #print(pac.Shell.list_obj_thread[0].__repr__())
    #thread = pac.Shell.list_obj_user[1].add_thread()
    #print(pac.Shell.list_obj_post[0].__repr__())
    #print(pac.Shell.list_obj_thread[0].__repr__())
    #pac.Shell.list_obj_thread[0].display()

    #post = pac.Post("coucou!!", pac.Shell.list_obj_user[1].name)
    #print(post.__repr__()[0])
    #alice = pac.Moderateur("jojo", "abab")

    #print(pac.Shell.list_posts)
    #print(pac.Shell.list_obj_user[1].name)

    #pac.Shell.list_obj_user[1].add_post(pac.Shell.list_obj_thread[0])
    #print(pac.Shell.list_obj_thread[0].obj_posts[0])
    #print(len(pac.Shell.list_obj_thread[0].obj_posts))

    #pac.seek(pac.Shell.list_posts[1], pac.Shell.list_posts, 'data_posts.csv')

    #print(pac.Shell.list_user)
    #print(pac.Shell.list_obj_user[1].__repr__())
    #print(pac.Shell.list_obj_post[0].__repr__())
    #print(pac.Shell.list_obj_thread[0].__repr__())
    #pac.modif_database(pac.Shell.list_obj_post[0], pac.Shell.list_obj_post, pac.Shell.list_posts, 'data_posts.csv', 'content_post', 'yopyop', pac.Shell.head_post)
    #print(pac.Shell.list_obj_post[0].__repr__())

    
    

if __name__ == "__main__":
    main()

        
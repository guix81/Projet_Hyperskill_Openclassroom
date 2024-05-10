import package as pac


def main():
    pac.init_main()
    #print(pac.Shell.list_user)
    #print(pac.Shell.list_posts)
    #print(pac.Shell.list_threads[0]['liste_id_post'])
    #print(pac.Shell.list_obj_user[0].__repr__())
    #print(pac.Shell.list_obj_post[0].__repr__())
    #print(pac.Shell.list_obj_thread[0].__repr__())
    #thread = pac.Shell.list_obj_user[1].add_thread()
    #pac.Shell.list_obj_user[-1].add_post(pac.Shell.list_obj_thread[0])
    #print(pac.Shell.list_obj_thread[0])
    #pac.Shell.list_obj_thread[0].display()
    #print(type(pac.Shell.list_obj_thread[0].list_id_posts))
    #print(type(pac.Shell.list_obj_thread[0].list_id_posts))
    #pac.Shell.list_obj_user[1].modif_post(pac.Shell.list_obj_post[4])
    pac.Shell.list_obj_user[1].del_post(pac.Shell.list_obj_post[4])
    
    

if __name__ == "__main__":
    main()

        
import package as pac


pac.init_database()
pac.init_obj()


post = pac.Post("go goole comme tous le monde!", pac.Shell.list_obj_user[1])
thread = pac.Thread("Comment faire des gâteau?", post, pac.Shell.list_obj_user[1])
print(thread.__str__())


        
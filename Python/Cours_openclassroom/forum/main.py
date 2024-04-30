import package as pac


pac.init_data_user()
pac.init_obj_user()

thread = pac.Shell.list_obj_user[1].add_thread()
thread.display()

        
"""
Take a break
going to load a video from youtube
set an alarm to take a break
"""
import webbrowser
import time
length_of_time = 60*60



def main():
        """
        Test Function
        :return:
        """
        counter = 0
        while counter < 3:
            delay = 5  #input("how long do you want to take a break?: ")
            time.sleep(delay)
            start_time = time.time()
            elapsed_time = time.time() - start_time
            while elapsed_time < length_of_time:
                elapsed_time = time.time() - start_time
            else:
                url = "https://youtu.be/Gc2u6AFImn8"
                webbrowser.open(url, new=1)
        counter += 1



if __name__ == '__main__':
    main()
    exit(0)

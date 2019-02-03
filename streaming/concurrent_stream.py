import subprocess
import signal

pid_arr = []

def sigint_handler(signum, frame):
    print("SIGINT caught")
    for i in range(1, len(pid_arr)):
        pid_arr[i](signal.SIGTERM)
        print("killed " + pid_arr[i])
        del pid_arr[i]
    print("all killed")

def main():
    signal.signal(signal.SIGINT, sigint_handler)

    #cm1 = "./audio-gst.sh &"
    cm2 = "./start-gst.sh &"

    #pid_arr.append(subprocess.call(cm1, shell=True))
    pid_arr.append(subprocess.Popen(cm2, shell=True))

    print("PID_array: " + str(pid_arr))



if __name__ == "__main__":
    main()


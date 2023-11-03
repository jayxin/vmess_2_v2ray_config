import base64
import sys
import datetime
import os


def base64_2_vmess_addr(argv):
    if len(argv) < 2:
        arg_desc = "{file name of the file downloaded from URL}"
        print(f"Usage: {argv[0]} {arg_desc}")
    else:
        time_stamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
        input_file_name = argv[1]
        output_file_name = f"out/vmess_addr_{time_stamp}.out"

        if os.path.exists("out") is not True:
            os.mkdir("out")

        for f in os.listdir("out"):
            os.remove(f"out/{f}")

        with open(input_file_name, "r") as in_f:
            encoded_string = in_f.read()

            decoded_bytes = base64.b64decode(encoded_string)
            decoded_string = decoded_bytes.decode("utf-8")

            with open(output_file_name, "w") as out_f:
                out_f.write(decoded_string)

        print(output_file_name)


if __name__ == "__main__":
    base64_2_vmess_addr(sys.argv)

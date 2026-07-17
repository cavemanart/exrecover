import pytsk3


class ImgInfo(
    pytsk3.Img_Info
):

    def __init__(self,path):

        self.path=path

        super().__init__()


    def read(
        self,
        offset,
        size
    ):

        with open(
            self.path,
            "rb"
        ) as f:

            f.seek(offset)

            return f.read(size)


    def get_size(self):

        return self.size



def scan_drive(device):

    results=[]

    img=ImgInfo(
        device
    )


    fs=pytsk3.FS_Info(
        img
    )


    directory=fs.open_dir(
        path="/"
    )


    for entry in directory:

        name=entry.info.name.name


        if name:

            results.append({

                "name":
                name.decode(
                    errors="ignore"
                ),

                "size":
                entry.info.meta.size

            })


    return results

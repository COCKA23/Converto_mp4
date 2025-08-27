import ffmpeg
import os
import subprocess
import sys


class Mp_gif():
    def __init__(self):
        self.dir_path = None
        self.fps = None



    '''Работа по конвертации в .gif и ascii'''


    def gif(self):
        


        gif_folder = os.path.join(self.dir_path, "gif")
        os.makedirs(gif_folder, exist_ok=True)

        # Проходим по файлам в директории
        for file in sorted(os.listdir(dir_path)):
            if file.lower().endswith(".mp4"):
                file_name = os.path.splitext(file)[0]
                input_path = os.path.join(dir_path, file)
                output_path = os.path.join(gif_folder, f"{file_name}.gif")
                palette_path = os.path.join(gif_folder, f"{file_name}_palette.png")

                # Создаем команду ffmpeg для конвертации
                (
                    ffmpeg
                    .input(input_path)
                    .filter('fps', fps=fps)
                    .filter('scale', 120, -1)
                    .filter('palettegen', max_colors=128)
                    .output(palette_path)
                    .overwrite_output()
                    .run(quiet=True)
                )


                stream = (
                    ffmpeg
                    .input(input_path)
                    .filter('fps', fps= fps)
                    .filter('scale', 120, -1)
                )

                (
                    ffmpeg
                    .filter([stream, ffmpeg.input(palette_path)], 'paletteuse', dither= 'bayer')
                    .output(output_path)
                    .overwrite_output()
                    .run(quiet= True)
                )
                

                os.remove(palette_path)
                print(f"Создан гиф: {output_path}")
            else:
                print(f"Пропускаю файл (не mp4): {file}")



    def smvd(self):
        pass


    def parameters(self):

        self.dir_path = input("Введите путь до директории: ")
        self.fps = input("Введите кол-во кадров в секунду (fps): ")
        try:
            self.fps = float(self.fps)
        except ValueError:
            print("Непиши хуйню. Установил 5 fps .")
            fps = 5

    def hemp_me(self):
        print("План скрипта:\n\t1) Ввод пути до директории\n\t2) Ввод количества FPS\nПотом появится папка с гифками.")


    def restart_programms(self):
        print("\nперезагрузка\n")

        python = sys.executable
        os.execl(python, python, *sys.argv)


    def run(self):
        print("Вы находитесь в скрипте по преобразованию видео (.mp4) в гиф (.gif), введите /gif или /help для работы.")
        command = input()

        if  command == "/gif":
            self.parameters()
            self.gif()
        elif command == "/help":
            self.hemp_me()
        elif command == "/smvd":
            self.smvd()



        #ПЕРЕЗАГРУКА
        self.restart_programms()
           


if __name__ == "__main__":
    gif = Mp_gif()
    gif.run()
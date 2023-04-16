import os

input_path = input("请输入需要拆分的合并后图片的路径：") # 输入合并后图片的路径
output_dir = input("请输入拆分后图片序列的保存路径：") # 输出拆分后图片序列的文件夹路径
grid_size = input("请输入拆分网格的行数和列数，用'x'连接：") # 用户输入拆分网格的行数和列数，比如 2x2、3x3
row_num, column_num = map(int, grid_size.strip().split('x'))

index = 0

# 创建输出文件夹
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

# 遍历输入路径下所有图片文件，执行图片拆分操作
for file in os.listdir(input_path):
  if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
    img_path = os.path.join(input_path, file)
    # 获取输入图片的宽和高
    iw, ih = os.popen('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}'.format(img_path)).read().split('x')
    iw, ih = int(iw.strip()), int(ih.strip())

    # 使用ffmpeg命令行工具进行图片拆分
    for y in range(row_num):
      for x in range(column_num):
        # 构建输出文件路径
        index += 1
        output_path = os.path.join(output_dir, f"{str(index).zfill(3)}.jpeg")
        # 拆分图片
        crop_w = iw / column_num
        crop_h = ih / row_num
        os.system('ffmpeg -i {} -vf "crop={}:{}:{}:{}" {}'.format(img_path, crop_w, crop_h, crop_w * x, crop_h * y, output_path))
        # 输出拆分后的图片序列路径
        print("图片 {} 拆分后的图片序列路径为：{}".format(file, output_path))
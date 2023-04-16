import os

# 定义输入图片序列的路径和输出合并后图片的路径
input_folder = input("请输入输入文件夹的路径：")
output_folder = input("请输入输出文件夹的路径：")
tile_size = input("请输入tile的大小，例如：2x2、3x3等：")

input_path = os.path.join(input_folder, '%3d.jpeg') # 输入图片序列的路径
output_path = os.path.join(output_folder, '%3d.jpeg') # 输出合并后图片的路径

# 创建输出文件夹
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# 使用ffmpeg命令行工具进行图片合并
os.system('ffmpeg -i {} -filter_complex "[0:v] tile={}" {}'.format(input_path, tile_size, output_path))

# 输出合并后的图片路径
print("合并后图片的路径为：{}".format(output_path))
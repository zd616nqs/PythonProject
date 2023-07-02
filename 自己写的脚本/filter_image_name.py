import os
import glob

def select_images(folder_path):
    # 获取所有png和jpg文件的路径
    image_paths = glob.glob(os.path.join(folder_path, "*.png")) + glob.glob(os.path.join(folder_path, "*.jpg"))
    # 字典用来存储每个前缀对应的优先级最高的文件
    image_dict = {}
    total_remove_count = 0
    for image_path in image_paths:
        # 获取文件名和后缀
        file_name = os.path.basename(image_path)
        file_name_without_ext = os.path.splitext(file_name)[0]
        # 如果后缀不在指定的四种后缀中，则跳过该文件
        if not any(file_name_without_ext.endswith(thumb_keyword) for thumb_keyword in [".pic_thumb", ".pic_thumb_preview", ".pic", ".pic_hd"]):
            continue
        # 获取文件的前缀
        file_prefix = os.path.splitext(file_name_without_ext)[0]
        thumb_word = os.path.splitext(file_name_without_ext)[1]
        # file_prefix = file_name_without_ext.split("_", 1)[1].rsplit(".", 1)[0]
        # 如果前缀已经在字典中，则根据优先级更新字典中的文件
        if file_prefix in image_dict:
            current_ext = image_dict[file_prefix][1]
            priorityList = [".pic_hd", ".pic", ".pic_thumb_preview", ".pic_thumb"]
            current_priority = priorityList.index(current_ext)
            new_priority = priorityList.index(thumb_word)
            if new_priority < current_priority:
                # 删除优先级低的文件
                os.remove(image_dict[file_prefix][0])
                image_dict[file_prefix] = (image_path, thumb_word)
                total_remove_count += 1
                print(f"\t✅ 【{total_remove_count}】移除重复图片 {image_path}")
            else:
                # 删除当前文件
                os.remove(image_path)
                total_remove_count += 1
                print(f"\t✅ 【{total_remove_count}】移除重复图片 {image_path}")
        else:
            image_dict[file_prefix] = (image_path, thumb_word)
    # 返回字典中的文件路径列表
    return [value[0] for value in image_dict.values()]


def verifyInputFilePath(folder_path) -> bool:
    if not os.path.isdir(folder_path):
        # 判断文件夹路径是否存在
        print(f"❌ 文件夹不存在！{folder_path}")
        return False
    elif not os.listdir(folder_path):
        # 判断文件夹是否为空
        print(f"❌ 是一个空文件夹！！{folder_path}")
        return False
    else:
        return True


def remove_quotes_and_space(s):
    if s.startswith("'") or s.startswith('"'):
        s = s[1:]
    if s.endswith("'") or s.endswith('"'):
        s = s[:-1]
    if s.endswith(":"):
        s = s[:-1]
    return s.rstrip()





if __name__ == "__main__":
    folder_path = input("请输入文件夹路径：")
    folder_path = remove_quotes_and_space(folder_path)
    result = verifyInputFilePath(folder_path)
    if result:
        # 筛选并保留优先级最高的图片文件
        selected_image_paths = select_images(folder_path)
        if not len(selected_image_paths):
            print('\n-----没有重复图片，无需去重！！！')
        else:
            print('\n-----全部文件处理完成！！！')

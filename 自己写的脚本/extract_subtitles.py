# -*- coding: utf-8 -*-

import os
import subprocess
# import json
# import shlex



def extract_subtitles_from_mp4_files(folder_path):
        
    
    # 记录没有字幕轨的视频名称
    no_subtitles_files = []
    
    # -----------------判断文件夹下是否有mp4文件-----------------
    totalMp4Files = []
    for index, temp_filename in enumerate(os.listdir(folder_path)):
        # 构造文件的绝对路径
        temp_file_path = os.path.join(folder_path, temp_filename)
        # 判断文件是否为MP4格式
        if os.path.isfile(temp_file_path) and temp_filename.endswith(".mp4") and not temp_filename.startswith("._"):
            totalMp4Files.append(temp_filename)
            
    if not len(totalMp4Files):
        print('❌ 警告：文件夹内没有视频文件！！！')
        return
    
    
    # -------------------遍历文件夹下的所有文件-----------------
    for index, filename in enumerate(totalMp4Files):
        print(f"【{index+1}/{len(totalMp4Files)}】开始处理....")
        print(f"\t 文件：{filename}")
        
        # 构造视频文件和字幕文件的绝对路径
        file_path = os.path.join(folder_path, filename)
        subtitle_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".srt")
        
        # 记录原始文件的路径
        origin_file_path = f'{file_path}'
        
        # 处理含有空格的文件名
        file_path = f'{file_path}'
        subtitle_file_path = f'{subtitle_file_path}'
        
        
        # --------------遍历所有视频流，判断是否包含字幕，使用FFmpeg probe功能获取视频信息--------------
        if os.path.isfile(subtitle_file_path):
            print(f"\t💊 字幕文件已存在，请删除后重试：{subtitle_file_path}")
            continue
        
        # has_sub_track = False
        # try:            
        #     escaped_path = shlex.quote(file_path)
        #     probe_cmd = f"ffprobe -v error -show_entries stream=index,codec_type -of json {escaped_path}"
        #     probe_result = subprocess.check_output(probe_cmd)
        #     streams = json.loads(probe_result)["streams"]
            
            
        #     for stream in streams:
        #         if stream.get("codec_type") == "subtitle":
        #             has_sub_track = True
        #             break
        # except subprocess.CalledProcessError as e:
        #     has_sub_track = False
        #     print(f"\n\n\n\nError while processing file {filename}: {e}\n\n\n\n")
        # except json.JSONDecodeError as e:
        #     has_sub_track = False
        #     print(f"\n\n\n\nError while decoding JSON for file {filename}: {e}\n\n\n\n")
            
        # if not has_sub_track:
        #     # 如果没有字幕轨道，则记录文件名
        #     no_subtitles_files.append(filename)
        #     print(f"\t❌ 视频没有字幕轨道，无法提取：{filename}")
        #     continue
        
        
        # ------------执行提取字幕操作----------
        cmd_extract = f'ffmpeg -i "{file_path}" -map 0:s:0 "{subtitle_file_path}" -v quiet'
        subprocess.call(cmd_extract, shell=True)
        if not os.path.isfile(subtitle_file_path):
            print(f"\t❌ 字幕提取失败：{filename}")
            continue
        print("\t✅ 提取并导出字幕文件成功！！")
        
        # ------------执行移除字幕轨，生成新文件，替换旧文件---------
        temp_output_file = os.path.join(folder_path, "temp_" + filename)
        cmd_remove_subtitle_track = f'ffmpeg -i "{file_path}" -map 0:v -codec copy -map 0:a -map -0:s -avoid_negative_ts make_zero "{temp_output_file}" -v quiet'
        subprocess.call(cmd_remove_subtitle_track, shell=True)
        if not os.path.isfile(origin_file_path):
            print(f'\t❌ 原视频不存在，请检查：{origin_file_path}')
            continue
        if not os.path.isfile(temp_output_file):
            print(f'\t❌ 临时视频不存在，请检查：{temp_output_file}')
            continue
        print("\t✅ 移除字幕轨，生成新的临时视频完成！！")
        
        
        # ------------新视频文件替换原有视频----------
        # 删除原视频文件
        os.remove(origin_file_path)
        # 重命名并替换文件
        os.rename(temp_output_file, origin_file_path)
        print("\t✅ 新老视频文件替换成功！！")
        
            

    print('\n', '-'*50, '\n', '-'*50)
    if no_subtitles_files:
        print("💊 以下视频文件没有字幕轨:")
        for filename in no_subtitles_files:
            print('  ', filename)
        print('\n-----全部文件处理完成！！！')
    else:
        print('\n-----全部文件处理完成！！！')
        



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



while True:
    folder_path = input("请输入文件夹路径：")
    folder_path = remove_quotes_and_space(folder_path)
    print(f'输入地址校验：{folder_path}-----')
    result = verifyInputFilePath(folder_path)
    if result:
        extract_subtitles_from_mp4_files(folder_path)
        break




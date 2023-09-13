import os
import librosa
import soundfile
from glob import glob


# 定义转换采样率的函数，接收3个变量：原音频路径、重新采样后的音频存储路径、目标采样率
def change_sample_rate(path, new_dir_path, new_sample_rate=24000):
    wavfile = path.split('/')[-1]
    signal, sr = librosa.load(path, sr=None)
    new_signal = librosa.resample(signal, sr, new_sample_rate)
    new_path = os.path.join(new_dir_path, wavfile)  # 指定输出音频的路径，音频文件与原音频同名
    print(new_path)

    soundfile.write(new_path, new_signal, new_sample_rate)


root_dir = '/data/msy/00_DATA/VCTK/wav48_silence_trimmed/'
spk_lst = [os.path.basename(i) for i in glob('/data/msy/00_DATA/VCTK/wav48_silence_trimmed/*')]
spk_lst.sort()
print(len(spk_lst))

for spk in spk_lst:
    #指定原音频文件夹路径
    original_path = f'/data/msy/00_DATA/VCTK/wav48_silence_trimmed/{spk}/'
    wav_list = os.listdir(original_path)
    wav_list.sort()

    #指定转换后的音频文件夹路径
    new_dir_path = f'/data/msy/00_DATA/VCTK/downsampled_wavs/{spk}/'
    os.makedirs(new_dir_path, exist_ok=True)

    #开始以对原音频文件夹内的音频进行采样率的批量转换
    for i in wav_list:
        wav_path = os.path.join(original_path, i)
        change_sample_rate(wav_path, new_dir_path, new_sample_rate=24000)
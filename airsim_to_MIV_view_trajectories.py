import os
import json
import pandas as pd
import time
from pathlib import Path
from sys import argv
from multiprocessing import Pool


def change_col_rpy_to_ypr(df_init):
    df_sort = pd.DataFrame()
    df_sort['X'] = df_init['x']
    df_sort['Y'] = df_init['y']
    df_sort['Z'] = df_init['z']
    df_sort['Yaw'] = df_init['yaw']
    df_sort['Pitch'] = df_init['pitch']
    df_sort['Roll'] = df_init['roll']
    return df_sort

def turn_face_dir(df_init):
    df_init['X'] = df_init['X'].mul(1)
    df_init['Y'] = df_init['Y'].mul(-1)
    df_init['Z'] = df_init['Z'].mul(-1)
    df_init['Yaw'] = df_init['Yaw'].mul(-1)
    df_init['Pitch'] = df_init['Pitch'].mul(-1)
    df_init['Roll'] = df_init['Roll'].mul(1)
    return df_init

def airsim_to_MIV(file_path):
    df_raw = pd.read_csv(file_path)
    df_sort = change_col_rpy_to_ypr(df_raw)
    df_turn = turn_face_dir(df_sort)
    return df_turn


def main():
    scenes = ['ArchVizInterior','LightroomInteriorDayLight','Office','RealisticRendering','XoioBerlinFlat']
    poses = [f'pose{i}' for i in range(6)]
    
    os.system(f'mkdir ./new_pose_trace')
    for scene in scenes:
        for pose in poses:
            os.system(f'mkdir ./new_pose_trace/{scene}')
            file_path = f'./{scene}/{pose}.csv'
            df = airsim_to_MIV(file_path)
            df.to_csv(f'./new_pose_trace/{scene}/{pose}.csv', index=False)

if __name__ == '__main__':
    main()
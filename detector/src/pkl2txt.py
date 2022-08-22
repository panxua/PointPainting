import pickle
import os 
from tqdm import tqdm

file_paths = ["detector/output/kitti_models/pointpillar_painted/default/eval/epoch_77/test/default/result.pkl"]
result_paths = ["detector/output/results/PLC/"]
for i, path in enumerate(file_paths):
    results_file = open(path,"rb")
    results = pickle.load(results_file)
    if not os.path.exists(result_paths[i]):
        os.makedirs(result_paths[i])
    for ret in tqdm(results):
        frame_id = ret['frame_id']
        file = open(result_paths[i]+"%s.txt"%frame_id,"w")
        for obj_idx, obj_name in tqdm(enumerate(ret['name']), total = len(ret['name']), leave=False):
            temp_ret = [obj_name, str(ret['truncated'][obj_idx]), str(ret['occluded'][obj_idx]), \
                str(ret['alpha'][obj_idx]), *map(str, ret['bbox'][obj_idx]), *(map(str, ret['dimensions'][obj_idx][[1,0,2]])), \
                *map(str, ret['location'][obj_idx]), str(ret['rotation_y'][obj_idx]), str(ret['score'][obj_idx]),]
            file.write(" ".join(temp_ret)+"\n")
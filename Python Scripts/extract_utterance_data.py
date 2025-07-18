import os
import re
import json
import pandas as pd

# Base path to the data folders
base_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/gemini_data_analysis/data/"
conference_folders = ["2021MND", "2021ABI", "2021SLU", "2021MZT"]

# Output: list of utterances
utterance_data = []

# Regex pattern to include only relevant session-level JSONs
valid_json_pattern = re.compile(r"\d{4}_\d{2}_\d{2}_.+_S\d+\.json")

for conf in conference_folders:
    conf_path = os.path.join(base_path, conf)
    print(f"\n🔍 Scanning: {conf_path}")

    for filename in os.listdir(conf_path):
        if filename.endswith(".json") and valid_json_pattern.match(filename):
            file_path = os.path.join(conf_path, filename)
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)

                session_id = filename.replace(".json", "")
                all_speakers = data.get("all_speakers", [])
                all_utterances = data.get("all_data", [])

                for utt in all_utterances:
                    utterance_data.append({
                        "conference": conf,
                        "session": session_id,
                        "speaker": utt.get("speaker"),
                        "timestamp": utt.get("timestamp"),
                        "speaking_duration": utt.get("speaking_duration"),
                        "nods_others": utt.get("nods_others"),
                        "smile_self": utt.get("smile_self"),
                        "smile_other": utt.get("smile_other"),
                        "distracted_others": utt.get("distracted_others"),
                        "hand_gesture": utt.get("hand_gesture"),
                        "interruption": utt.get("interuption"),
                        "overlap": utt.get("overlap"),
                        "screenshare": utt.get("screenshare"),
                        "annotations": utt.get("annotations", {}),
                        "transcript": utt.get("transcript")
                    })

            except Exception as e:
                print(f"⚠️ Failed to process {filename}: {e}")

# Convert to DataFrame and save
df_utterances = pd.DataFrame(utterance_data)
output_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/Data/extracted_utterance_data.csv"
df_utterances.to_csv(output_path, index=False)

print(f"\n Saved {len(df_utterances)} utterances to {output_path}")

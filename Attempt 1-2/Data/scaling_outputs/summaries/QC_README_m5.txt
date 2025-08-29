QC instructions (m≥5, W=±20.0s)

• Open QC_bursts_list_m5.csv in Google Sheets or Excel.
• For each row (one burst), skim the teaser_context.
• If unclear, look up the full window in QC_burst_context_m5.csv 
  (filter by the same conference, session, center_time_sec).
• Then fill:
  - human_is_decision: Y or N (does this window contain a real decision moment?)
  - human_decision_type: assignment / choice / plan / consensus / summary / other
  - human_initiator: who kicked off the decision (speaker name or 'multiple')
  - human_confidence_1to5: 1 (low) .. 5 (high)
  - human_notes: any nuance you'd like to capture
• Save your edits to a NEW file: QC_bursts_list_m5_ANNOTATED.csv

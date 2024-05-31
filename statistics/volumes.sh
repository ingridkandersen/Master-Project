# This script computes the volumetric changes for the different segmentations for all timepoints and all participants 
# Fill out for every participant 

asegstats2table \
-i Kontroll/recon_results/FXXXXX/FXXXXX_tp1.long.FXXXXX_base/stats/aseg.stats \
Kontroll/recon_results/FXXXXX/FXXXXX_tp2.long.FXXXXX_base/stats/aseg.stats \
Kontroll/recon_results/FXXXXX/FXXXXX_tp3.long.FXXXXX_base/stats/aseg.stats \
Kontroll/recon_results/FXXXXX/FXXXXX_tp4.long.FXXXXX_base/stats/aseg.stats \
ECT/recon_results/FYYYYY/FYYYYY_tp1.long.FYYYYY_base/stats/aseg.stats \
ECT/recon_results/FYYYYY/FYYYYY_tp2.long.FYYYYY_base/stats/aseg.stats \
ECT/recon_results/FYYYYY/FYYYYY_tp3.long.FYYYYY_base/stats/aseg.stats \
ECT/recon_results/FYYYYY/FYYYYY_tp4.long.FYYYYY_base/stats/aseg.stats \
TMS/recon_results/FZZZZZ/FZZZZZ_tp1.long.FZZZZZ_base/stats/aseg.stats \
TMS/recon_results/FZZZZZ/FZZZZZ_tp2.long.FZZZZZ_base/stats/aseg.stats \
TMS/recon_results/FZZZZZ/FZZZZZ_tp3.long.FZZZZZ_base/stats/aseg.stats \
TMS/recon_results/FZZZZZ/FZZZZZ_tp4.long.FZZZZZ_base/stats/aseg.stats \
TMS/recon_results/FZZZZZ/FZZZZZ_tp5.long.FZZZZZ_base/stats/aseg.stats \
--meas volume \
--tablefile asegstats.txt 

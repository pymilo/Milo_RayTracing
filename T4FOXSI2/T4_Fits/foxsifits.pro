
loadct, 2
reverse_ct
trange=[t4_start,t4_end]
m0 = foxsi_image_map( data_lvl2_d0, cen4, erange=[5.,10.], trange=trange, thr_n=4., /xycorr )
plot_map, m0, /limb, lcol=255, col=255, charsi=1.2, title=m0.id
draw_fov,det=0,target=4
map2fits,m0,'foxsi_T4_d0.fits'

loadct, 2
reverse_ct
trange=[t4_start,t4_end]
m1 = foxsi_image_map( data_lvl2_d1, cen4, erange=[5.,10.], trange=trange, thr_n=4., /xycorr )
plot_map, m1, /limb, lcol=255, col=255, charsi=1.2, title=m1.id
draw_fov,det=1,target=4
map2fits,m1,'foxsi_T4_d1.fits'

loadct, 2
reverse_ct
trange=[t4_start,t4_end]
m4 = foxsi_image_map( data_lvl2_d4, cen4, erange=[5.,10.], trange=trange, thr_n=4., /xycorr )
plot_map, m4, /limb, lcol=255, col=255, charsi=1.2, title=m4.id
draw_fov,det=4,target=4
map2fits,m4,'foxsi_T4_d4.fits'


loadct, 2
reverse_ct
trange=[t4_start,t4_end]
m5 = foxsi_image_map( data_lvl2_d5, cen4, erange=[5.,10.], trange=trange, thr_n=4., /xycorr )
plot_map, m5, /limb, lcol=255, col=255, charsi=1.2, title=m5.id
draw_fov,det=5,target=4
map2fits,m5,'foxsi_T4_d5.fits'

loadct, 2
reverse_ct
trange=[t4_start,t4_end]
m6 = foxsi_image_map( data_lvl2_d6, cen4, erange=[5.,10.], trange=trange, thr_n=4., /xycorr )
plot_map, m6, /limb, lcol=255, col=255, charsi=1.2, title=m6.id
draw_fov,det=6,target=4
map2fits,m6,'foxsi_T4_d6.fits'






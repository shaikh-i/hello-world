%% Filenames changed to maintain user privacy 
%% pre function commands
close all;
clc;
clear;
load("C:\Users\Username\Desktop\NCBL\Data.mat");
fid = fopen("test2.txt",'w+');
%% function commands
imgn = 40;
for x = 1:imgn
    for z = ((x*160)-15):x*160
        for y = 1:16
            fprintf(fid, '%d\n', FSA_pressure(z,y));
        end
    end
end
%% post function commands
fclose(fid);
fprintf("Success! Copy command complete. \n")

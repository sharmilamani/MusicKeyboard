%  Electromyography (EMG) Feature Extraction toolbox
% Generate all features
%---------------------------------------------------------------------
%% Extract all features
% Generate a sample random signal X
path = "H:\My Drive\ColabNotebooks\Data\2022_60Trials_InstantPressAndRelease\";
fingers = ["1T", "2I", "3M", "4R", "5L"];

feat = ["emav", "ewl", "fzc","asm", "ass","msr", "ltkeo", "lcov", "card", "ldasdv", "ldamv", "dvarv","vo","tm","damv","ar","mad","iqr","skew","kurt","cov","sd","var","ae","iemg","mav","ssc","zc","wl","rms","aac","dasdv","ld","mmav","mmav2","myop","ssi","vare","wa","mfl"];
N = length(feat);
header = ["emav", "ewl", "fzc","asm", "ass","msr", "ltkeo", "lcov", "card", "ldasdv", "ldamv", "dvarv","vo","tm","damv","ar1","ar2", "ar3", "ar4", "mad","iqr","skew","kurt","cov","sd","var","ae","iemg","mav","ssc","zc","wl","rms","aac","dasdv","ld","mmav","mmav2","myop","ssi","vare","wa","mfl"];
featureLength = 196;

for class = fingers
    dirContents = dir(path + class + "\emg*.csv");    
    feature_path = "D:\Features_" + class + ".xls";
    fprintf("%s\n", feature_path);
    writematrix(header,feature_path,'WriteMode', 'overwrite');
    for file = dirContents'
        filename_path = strcat(file.folder, "\");
        filename_path = strcat(filename_path, file.name);
        %fprintf("%s\n", filename_path);

        options = detectImportOptions(filename_path);
        %preview('H:\MyDrive\1T\emg-1648376191.csv', options);
        options.SelectedVariableNames = 3; %emg2 at 3 column
        options.range="2:198c";
        
        mat = readmatrix(filename_path, options);
        %disp(mat);
        
        feature = zeros(N+3,1); %4 values in ar so N+3
        index = 1;
        for i = 1:N
            %TODO : all features are assigned default value. if required modify after feature analysis
            val =jfemg(feat(i), mat);
            len = length(val);
            fprintf("{%s=%d, %f}\n", feat(i),len,val);
            if (len == 1)
                feature(index) = val;
                index = index +1;
            else 
                for j = 1 : len
                    feature(index) = val(1,j);
                    index = index+1;
                end
            end
        end
        feature_T =  reshape(feature,[1 length(feature)]); %to make features to be added rowwise
        writematrix(feature_T,feature_path,'WriteMode', 'append');
    end
end



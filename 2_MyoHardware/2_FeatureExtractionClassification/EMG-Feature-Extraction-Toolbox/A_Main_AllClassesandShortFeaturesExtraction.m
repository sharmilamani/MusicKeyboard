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
framesize = 50;
overlap = (50/100)*framesize; %50 percent overlap

for class = fingers
    dirContents = dir(path + class + "\emg*.csv");    
    feature_path = "D:\Features_" + class + ".xls";
    fprintf("Feature Path %s\n", feature_path);
    writematrix(header,feature_path,'WriteMode', 'overwrite');
    
    for file = dirContents'
        filename_path = strcat(file.folder, "\");
        filename_path = strcat(filename_path, file.name);
        fprintf("filenamepath = %s\n", filename_path);

        options = detectImportOptions(filename_path);        
        options.SelectedVariableNames = 3; %emg2 at 3 column
        %options.range = "2:198c";
        options.DataLines = [2 198];        
        options.VariableNamesLine =0;
       
        feature = zeros(N+3,1); %4 values in ar so N+3

        mat = readmatrix(filename_path, options);        
        preview(filename_path, options);
        %preview('H:\Data\1T\emg-1648376191.csv', options);
        size_mat =  size(mat);
        mat_length = size_mat(1,1);
        fprintf("Matrix Size %d %d\n", mat_length, maxsize);

        fl = 1;
        maxsize = 1;
        % to check frame window start point i.e f1 reached max and end point i.e maxsize reached
        % end during overlap > 0
        while (fl < mat_length) && (maxsize ~= mat_length)
            maxsize = fl + framesize;
         
            if (maxsize > mat_length)
                % since last frame is only till 197 not a multiple of
                % framesize 50 copy the remaining from 151 to 197 
                maxsize = mat_length;
                smat(1:maxsize-fl) = mat(fl:maxsize-1);                
            else
                smat(1:framesize) = mat(fl: maxsize-1);
            end

            fprintf("Features of [%d, %d]\n", fl, maxsize-1);
            fl = maxsize-overlap;

            for i = 1:N
                %TODO : all features are assigned default value. if required modify after feature analysis
                val =jfemg(feat(i), smat);
                len = length(val);
                %fprintf("{%s=%d, %f}\n", feat(i),len,val);
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
            index = 1;

            feature_T =  reshape(feature,[1 length(feature)]); %to make features to be added rowwise
            writematrix(feature_T,feature_path,'WriteMode', 'append');        
        end        
    end
end
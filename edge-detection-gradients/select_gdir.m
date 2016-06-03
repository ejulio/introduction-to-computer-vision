% Gradient Direction
function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
    result = gmag >= mag_min & angle_low <= gdir & gdir <= angle_high;
    %result = zeros(size(gmag));
    
    %for i = 1:size(gmag, 2)
    %  for j = 1:size(gmag, 1)
    %    if gmag(j, i) >= mag_min && gdir(j, i) >= angle_low && gdir(j, i) <= angle_high
    %      result(j, i) = gmag(j, i);
    %    end
    %  end
    %end
      
    %result = result / (4 * sqrt(2));
    % TODO Find and return pixels that fall within the desired mag, angle range

endfunction
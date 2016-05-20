# combine obstruent and vowel measurements

def main():

	# grab the data
	file = open('obstr_new.txt')
	obstr = file.readlines()
	obstr.sort()
	file.close()
	file = open('vowel_new.txt')
	vowel = file.readlines()
	vowel.sort()
	file.close()

	# open the output file
	out = open('combined.txt', 'w')

	# indices
	obs_idx = 0
	vow_idx = 0
	obs_data = obstr[obs_idx].rstrip().split('\t')
	obs_ident = obs_data[0].split('+')
	vwl_data = vowel[vow_idx].rstrip().split('\t')
	vwl_ident = vwl_data[0].split('+')
	if vwl_ident[0] == obs_ident[0] && vwl_ident[1] == obs_ident[1] && abs(float(vwl_ident[2])-float(obs_ident[2])) < 1:
		out.write('%s\t%s\n' % (obs_data[0], '\t'.join(obs_data[1:]+vwl_data[1:])))
		obs_idx += 1
		vow_idx += 1
	elseif obs_data[0] < vwl_data[0]:
		obs_idx += 1
	else:
		vow_idx += 1
	
	# done
	out.close()

if __name__ == '__main__':
	main()
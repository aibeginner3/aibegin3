;#
;#再帰表示
;#
 
use strict;
 
#-- 再帰実行 --#
my @files;
reflexiveFile('.');
 
#-------------------------------------------#
#■ディレクトリ配下を全て表示
#-------------------------------------------#
sub reflexiveFile{
  my $dir = shift;
  my @list = ();
 
  #-- カレントの一覧を取得 --#
  opendir(DIR, $dir) or die("Can not open directory:$dir ($!)");
  @list = readdir(DIR);
  closedir(DIR);
 
  foreach my $file (sort @list){
    next if( $file =~ /^\.{1,2}$/ );  # '.' と '..' はスキップ
 
    #-- ディレクトリの場合は自分自身を呼び出す --#
    if( -d "$dir/$file" ){
      reflexiveFile("$dir/$file");
    }
    #-- それ以外は表示 --#
    else{
      #print "$dir/$file\n";
      push(@files, "$dir/$file");
    }
  }

}

#print "@files";
foreach my $path (@files){
  next unless $path=~/.pl/;
  print "$path\n";

  open(IN, $path) or die;
  foreach my $line (<IN>){
    print "$line\n" if $line=~/list/;
  }
  close IN;
}


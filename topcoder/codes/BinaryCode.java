import java.util.*;
public class BinaryCode {
  String get(String message, int curr) {
    String r = "";
    int n = message.length();
    int prev = 0;
    int next = 0;
    for (int i = 0; i < n; i++) {

      //http://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1026085295
      //このサイトで謎が解ける。
      //char型をint型に変換する方法。- '0'をするとその変換が行える。
      int q = message.charAt(i) - '0';
      // charはStringの一文字だけversion

      //次のPは、今のqから前のpと今のpを引いたもの
      next = q - prev - curr;
      if (next < 0 || next > 1) return "NONE";
      r = r + curr;
      
      prev = curr; curr = next;
    }
    
    if (next != 0) return "NONE";
    
    return r;
  }
  
  public String[] decode(String message) {
    String [] r = new String[2];
    r[0] = get(message, 0);
    r[1] = get(message, 1);
    return r;
  }
 
 
 
 
 
 
}
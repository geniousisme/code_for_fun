class Game(object):
      def __init__(self, bowl_times):
          self.bowl_times = bowl_times
          self.frame_bowls = []
          self.frame_score = []
      
      def collect_to_frame(self, bowl_counts):
          frame_count = 1
          i           = 0
          while i < self.bowl_times - 1 and frame_count < 10:
            if bowl_counts[i] == 10:
                self.frame_bowls.append([bowl_counts[i], 0])
                i += 1
            else:
                self.frame_bowls.append([bowl_counts[i], bowl_counts[i + 1]])
                i += 2
            frame_count += 1
          self.frame_bowls.append(bowl_counts[i:])

      def isStrike(self, frame_idx):
          return self.frame_bowls[frame_idx][0] == 10 or                       \
                 self.frame_bowls[frame_idx][1] == 10
          
      def score(self):
          frame_num = len(self.frame_bowls)

          for i in xrange(frame_num):
              self.frame_score.append(sum(self.frame_bowls[i]))
          
          for i in xrange(frame_num - 2):
              if self.frame_score[i] == 10: # strike or spare
                 if self.isStrike(i): # strike
                    if self.isStrike(i + 1):
                        self.frame_score[i] += 10
                        if self.isStrike(i + 2):
                            self.frame_score[i] += 10
                        else:
                            self.frame_score[i] += self.frame_score[i + 2][0]
                    else:
                        self.frame_score[i] += sum(self.frame_score[i + 1])
              else: # spare
                 self.frame_score[i] += self.frame_bowls[i][0]
          i = 8
          if self.frame_score[i] == 10:
             if self.isStrike(i):
                self.frame_score[i] += self.frame_bowls[i + 1][0] +            \
                                       self.frame_bowls[i + 1][1]
             else:
                self.frame_score[i] += self.frame_bowls[i + 1][0]
          return sum(self.frame_score)
          
if __name__ == '__main__':
   bowl_times = int(raw_input())
   g = Game(bowl_times)
   bowl_counts = []
   for i in xrange(bowl_times):
       bowl_counts.append(int(raw_input()))
   g.collect_to_frame(bowl_counts)
   print g.score()
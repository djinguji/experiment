def quiz_script(args):
    return'''
<script>
total = {0};
'''.format(args.total) + '''
function compose() {
  var len = document.scores.done.length;
  var done = 0;
  var score = 0;
  var missing = 0;
  var comp = \'''' + args.nl + '''Completed:';
  for(var i = 0; i < len; i ++) {
    if( ! document.scores.done[i].checked) {
      missing ++;
    } else {
      var pt = 1;
      if(document.scores.done[i].hasAttribute('points')) {
        pt = parseInt(document.scores.done[i].getAttribute('points'));
      }
      score += pt;
      done ++;
      comp += \'''' + args.nl + ''' * ' + document.scores.done[i].value;
    }
  }
  var msg;
  if(done == 0) {
    msg = \'''' + args.startp + '''None completed in this set.';
  } else if(score < total/2) {
    msg = \'''' + args.startp + '''Good start.';
  } else {
    msg = \'''' + args.startp + '''Good work.';
  }
  if(score) {
    msg += comp;
  }
  if(missing && done && document.scores.inclmiss.checked) {
    msg += \'''' + args.nl + '''Missing:';
    for(var i = 0; i < len; i ++) {
      if( ! document.scores.done[i].checked) {
        msg += \'''' + args.nl + ''' * ' + document.scores.done[i].value;
      }
    }
  }
  msg += \'''' + args.endp + '''';
  document.scores.score.value = score + '/' + total;
  document.scores.comments.value = msg;
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function nonedone() {
  document.scores.score.value = '0/' + total;
  document.scores.comments.value = \'''' + args.startp + '''Nothing submitted.''' + args.endp + '''';
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function setall() {
  document.scores.score.value = '';
  document.scores.comments.value = '';
  var len = document.scores.done.length;
  for(var i = 0;i < len; i ++) {
    document.scores.done[i].checked = true;
  }
}
function clear() {
  document.scores.score.value = '';
  document.scores.comments.value = '';
  var len = document.scores.done.length;
  for(var i = 0;i < len; i ++) {
    document.scores.done[i].checked = false;
  }
}
</script>
'''

def codingbat_script(args):
    return'''
<script>
total = {0};
'''.format(args.total) + '''
function doneclick(n) {
  if( ! document.scores.done[n].checked) {
    document.scores.late[n].checked = false;
  }
}
function lateclick(n) {
  if(document.scores.late[n].checked) {
    document.scores.done[n].checked = true;
  }
}

function noacct() {
  document.scores.score.value = '0/' + total;
  document.scores.comments.value = \'''' + args.startp + '''No CodingBat account found.''' + args.endp + '''';
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function nonedone() {
  document.scores.score.value = '0/' + total;
  document.scores.comments.value = \'''' + args.startp + '''None completed in this set.''' + args.endp + '''';
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function compose() {
  var len = document.scores.done.length;
  var done = 0;
  var score = 0;
  var missing = 0;
  var late = 0;
  var comp = \'''' + args.nl + '''Completed:';
  for(var i = 0; i < len; i ++) {
    if( ! document.scores.done[i].checked) {
      missing ++;
    } else if(document.scores.late[i].checked) {
      late ++;
      done ++;
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
  var msg = \'''' + args.startp + '''';
  if(done == 0) {
    msg += 'None completed in this set.';
  } else if(score < total/2) {
    msg += 'Good start.';
  } else {
    msg += 'Good work.';
  }
  if(score && document.scores.incldone.checked) {
    msg += comp;
  }
  if(score > total) {
    msg += \'''' + args.nl + ''' * Extra credit awarded';
  }
  if(missing && done) {
    msg += \'''' + args.nl + '''Missing:';
    for(var i = 0; i < len; i ++) {
      if( ! document.scores.done[i].checked) {
        msg += \'''' + args.nl + ''' * ' + document.scores.done[i].value;
      }
    }
  }
  if(late && done) {
    msg += \'''' + args.nl + '''Late:';
    for(var i = 0; i < len; i ++) {
      if(document.scores.late[i].checked) {
        msg += \'''' + args.nl + ''' * ' + document.scores.late[i].value;
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

function setall() {
  document.scores.score.value = '';
  document.scores.comments.value = '';
  var len = document.scores.done.length;
  for(var i = 0;i < len; i ++) {
    document.scores.late[i].checked = false;
    document.scores.done[i].checked = true;
  }
}
function clear() {
  document.scores.score.value = '';
  document.scores.comments.value = '';
  var len = document.scores.done.length;
  for(var i = 0;i < len; i ++) {
    document.scores.done[i].checked = false;
    document.scores.late[i].checked = false;
  }
}
</script>
'''

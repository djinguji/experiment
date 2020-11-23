def lab_script(args):
    return'''
<script>
total = {0};
choice = 0;
'''.format(args.total) + '''
function compose(head) {
  var msg = \'''' + args.startp + '''';
  msg += head;
  var score = 0;
''' + args.comp + '''
  msg += \'''' + args.endp + '''';
  document.scores.score.value = score + '/' + total;
  document.scores.comments.value = msg;
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function clear_form() {
''' + args.clr + '''
  document.scores.score.value = '';
  document.scores.comments.value = '';
  document.scores.s1[0].focus();
}

function nonedone() {
  document.scores.score.value = '0/' + total;
  document.scores.comments.value = \'''' + args.startp + 'Nothing submitted.' + args.endp + '''';
  document.scores.comments.select();
  document.execCommand('copy');
  document.scores.comments.focus();
}

function compose_item(cbs, title) {
  var msg = '';
  var len = cbs.length;
  var ct = 0;
  for(var i = 0; i < len; i++) {
    if(cbs[i].checked) {
	  if(ct) {
	    msg += ', ' + cbs[i].value;
	  } else {
	    msg += cbs[i].value;
	  }
	  ct ++;
	}
  }
  if(ct) {
    msg = \'''' + args.nl + '''' + title + ': ' + msg;
  }
  return msg;
}

function compose_array(cbs) {
  var msg = '';
  var len = cbs.length;
  for(var i = 0; i < len; i++) {
    if(cbs[i].checked) {
	  msg += \'''' + args.nl + ''' * ' + cbs[i].value;
	}
  }
  return msg;
}

function compose_array_2(cbs, blanks) {
  var msg = '';
  var len = cbs.length;
  for(var i = 0; i < len; i++) {
    if(cbs[i].checked) {
	  msg +=\'''' + args.nl + ''' * ' + blanks[i].value;
	}
  }
  return msg;
}

function cleararray(obj) {
  var len = obj.length;
  for(var i = 0; i < len; i ++) {
    obj[i].checked = false;
  }
}

</script>
'''

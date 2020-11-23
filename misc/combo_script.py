def combo_script(args):
    return'''
<script>
total = {0};
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

function nosubmit() {
  document.scores.score.value = '0/' + total;
  document.scores.comments.value = \'''' + args.startp + '''Nothing submitted.''' + args.endp + '''';
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

function clear_form() {
''' + args.clr + '''
  document.scores.score.value = '';
  document.scores.comments.value = '';
  document.scores.s1[0].focus();
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

function cleararray(obj) {
  var len = obj.length;
  for(var i = 0; i < len; i ++) {
    obj[i].checked = false;
  }
}

function setarray(obj) {
  var len = obj.length;
  for(var i = 0; i < len; i ++) {
    obj[i].checked = true;
  }
}

</script>
'''
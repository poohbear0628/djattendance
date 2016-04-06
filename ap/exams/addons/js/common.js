function fttaUrl(path) {
	return dojo.uri.joinPath(ftta.rootDirectory||"", path);
}

var Elm = {
	next: function(node) {
		node = dojo.byId(node);
		if(node) {
			do {
				node = node.nextSibling;
			} while(node && node.nodeType != 1);
		}
		return node;
	},

	prev: function(node) {
		node = dojo.byId(node);
		if(node) {
			do {
				node = node.previousSibling;
			} while(node && node.nodeType != 1);
		}
		return node;
	},

	first: function(node) {
		node = dojo.byId(node);
		if(node) {
			node = Elm.next(node.firstChild);
		}
		return node;
	},

	last: function(node) {
		node = dojo.byId(node);
		if(node) {
			node = Elm.prev(node.lastChild);
		}
		return node;
	}
};

function nodeDepth(node, ancestor) {
	ancestor = dojo.byId(ancestor) || dojo.body();
	node = dojo.byId(node);

	var depth = 0;
	while(node && node != ancestor) {
		node = node.parentNode;
		depth++;
	}

	if(!node) { depth = -1; }

	return depth;
}

function toggleDevInfo() {
	if(dojo.html.toggleDisplay("dev-info")) {
		dojo.byId("dev-info").scrollIntoView(false);
	}
}

function toggleBugInfo() {
	if(dojo.html.toggleDisplay("bug-info")) {
		dojo.byId("bug-info").scrollIntoView(false);
	}
}

function confirmDelete(type) {
	return confirm("Are you sure you want to delete this " + type + "?");
}

function clearIfDefault(input) {
	if(input && input.value && input.defaultValue) {
		if(input.value == input.defaultValue) {
			input.value = "";
		}
	}
}

function restoreIfDefault(input) {
	if(input && input.value && input.defaultValue) {
		if(input.value != input.defaultValue) {
			input.value = input.defaultValue;
		}
	}
}

function toggleChecked(form, field) {
	if(arguments.length == 1) {
		// assume we're given the field obj of one of the checkboxes
		form = field.form;
		field = field.name;
	} else {
		form = dojo.lang.isString(form) ? document.forms[form] : form;
	}

	var cbs = form[field];
	if(isNaN(cbs.length)) {
		cbs = [cbs];
	}

	var totalChecked = 0;
	for(var i = 0; i < cbs.length; i++) {
		if(cbs[i].checked) { totalChecked++; }
	}

	for(var i = 0; i < cbs.length; i++) {
		cbs[i].checked = (totalChecked != cbs.length)
	}
}

function hideSlowLoading() {
	dojo.html.removeNode(dojo.byId("slow-loading"));
}

/* Ajax Throbber action
************************/
function Throbber(txt, dark, inline) {
	this.node = document.createElement(inline ? "span" : "div");
	this.node.className = "throbber" + (dark ? "dark" : "");
	this.setLabel(txt || "Loading...");
}
dojo.lang.extend(Throbber, {
	btn : null,

	setLabel : function(txt) {
		this.node.innerHTML = txt;
	},

	lockButton : function(btn) {
		btn.disabled = true;
		this.btn = btn;
	},

	unlockButton : function(btn) {
		var b = btn || this.btn;
		if(b) { b.disabled = false; }
	},

	insertBefore: function(node) {
		dojo.html.insertBefore(this.node, node);
	},

	insertAfter: function(node) {
		dojo.html.insertAfter(this.node, node);
	},

	append: function(node) {
		node.appendChild(this.node);
	},

	prepend: function(node) {
		dojo.html.prependChild(this.node, node);
	},

	done : function() {
		dojo.html.removeNode(this.node);
		this.unlockButton();
		this.node = null;
	}
});



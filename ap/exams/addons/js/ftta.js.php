<?php
header('Content-Type: text/javascript');
require_once('../../inc.session.php');
?>

if(typeof ftta == "undefined") {
	ftta = {};
}

ftta.userID = Number("<?php print $_SESSION['myID']; ?>");
ftta.rootDirectory = "<?php print $_SESSION['rootDirectory']; ?>";
ftta.ppc = <?php print $_SESSION['ppc'] ? "true" : "false"; ?>;

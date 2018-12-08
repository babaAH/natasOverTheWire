<?php

$cook = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$cook = base64_decode($cook);
//echo $cook;
function xor_encrypt($in) {

    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

echo xor_encrypt($cook);

?>

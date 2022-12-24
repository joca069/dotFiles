
Workspaces(){
	
	workspaces=(
	"$(herbstclient tag_status | awk '{ print $1}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $2}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $3}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $4}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $5}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $6}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $7}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $8}'| awk '{print substr($0,0,1)}')"
	"$(herbstclient tag_status | awk '{ print $9}'| awk '{print substr($0,0,1)}')"
	)
	
	
	ret=""

	for i in ${!workspaces[@]}; do
		
		case ${workspaces[$i]} in
		":")
			#tab with something in it
			ret="$ret%{A:herbstclient use $(($i+1)):}  %{A}"
		;;
		"#")
			#When tab is selected
			ret="$ret%{A:herbstclient use $(($i+1)):}  %{A}"
		;;
		".")
			#empty tab
			ret="$ret%{A:herbstclient use $(($i+1)):}  %{A}"
		;;
	
		esac

	done
	echo "$ret"
}



while true; do
    echo  "%{c}$(Workspaces) "
	sleep 0.2
done


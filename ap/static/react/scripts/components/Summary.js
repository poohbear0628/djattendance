import React, { PropTypes } from 'react'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'

const Summary = ({...p}) => {
  return (
  	<div>
  		<div className="legend"> 

  		</div>
  		<h5>Roll Events</h5>
	    <table className='table table-condensed'>
	    	<tbody>
		    	<tr>
		    		<th>Date</th>
		    		<th>Event</th>
		    	</tr>
		      {p.eventsRolls.map(esr =>
		        <RollDetail key={esr.event.start}
		          {...esr}
		        />
		      )}
	      </tbody>
	    </table>
	    <h5>Leave Slips</h5>
    	<table className='table table-condensed'>
	    	<tbody>
		    	<tr>
		    		<th>Type</th>
		    		<th>Status</th>
		    		<th>Actions</th>
		    	</tr>
		    	{p.groupslips.map(ls => {
		    		console.log(ls);
		        <LeaveSlipDetail key={ls.id}
		          ls={ls}
		        />
		      }
		      )}
		      {p.leaveslips.map(ls =>
		        <LeaveSlipDetail key={ls.id}
		          ls={ls}
		        />
		      )}

	      </tbody>
	    </table>
    </div>
  )
}

Summary.propTypes = {
}

export default Summary

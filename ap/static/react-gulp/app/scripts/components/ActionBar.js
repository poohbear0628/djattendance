import React, { PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SelectedEvent from './SelectedEvent'
import RollSlipForm from './RollSlipForm'
import GroupLeaveSlipForm from './GroupLeaveSlipForm'

const ActionBar = ({submitRollShow, submitLeaveSlipShow, submitGroupLeaveSlipShow, otherReasonsShow, leaveSlipDetailsShow,
                    selectedEvents, formSuccess, trainee, tas,
                    toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip, toggleOtherReasons,
                    removeSelectedEvent, removeAllSelectedEvents, postRollSlip, postGroupLeaveSlip }) => {
  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }

  var hideRoll = {};
  if (trainee.term[trainee.term.length-1] <= 2) {
    hideRoll = {display: "none"};
  }

  var lsdShow = false;
  for (var key in leaveSlipDetailsShow) {
    if (leaveSlipDetailsShow.hasOwnProperty(key) && leaveSlipDetailsShow[key]) {
      lsdShow = true;
      break;
    }
  }
  return (
    <div style={{marginBottom: "10px"}}>
    {/*Form control buttons*/}
      <div>
        <Button className="action-button" onClick={toggleSubmitRoll} style={hideRoll}>Roll</Button>
        <Button className="action-button" onClick={toggleSubmitLeaveSlip}>Leave Slip</Button>
        <Button className="action-button" style={{display: "none"}} onClick={toggleSubmitGroupLeaveSlip}>Group Leave Slip</Button>
      </div>
    {/*Sessions selected*/}
      <div>
        <Collapse in={(selectedEvents.length > 0 || submitRollShow || submitLeaveSlipShow) && (!lsdShow)}>
          <div className="form-body">
            <div className="form-section">
              <div className="toggle-title">
                Sessions Selected
                <Button bsSize="small" className={disabledClass} onClick={removeAllSelectedEvents}>Remove All</Button>
              </div>
              <div>
                {selectedEvents.map(function(ev) {
                  return <SelectedEvent
                            {...ev}
                            onClick={() => removeSelectedEvent(ev)}
                            selectedEvents={selectedEvents}
                          />
                })}
              </div>
            </div>
          </div>
        </Collapse>
      </div>
    {/*Roll and slip form*/}
      <div>
        <RollSlipForm
          post={(rollSlip) => postRollSlip(rollSlip, selectedEvents, null)}
          submitRollShow={submitRollShow}
          submitLeaveSlipShow={submitLeaveSlipShow}
          toggleSubmitLeaveSlip={() => toggleSubmitLeaveSlip()}
          toggleOtherReasons={() => toggleOtherReasons()}
          otherReasonsShow={otherReasonsShow}
          tas={tas}
        />
      </div>
    {/*Group slip form*/}
      <div>
        <GroupLeaveSlipForm
          post={(groupLeaveSlip) => postGroupLeaveSlip(groupLeaveSlip, selectedEvents)}
          submitGroupLeaveSlipShow={submitGroupLeaveSlipShow}
          toggleSubmitGroupLeaveSlip={() => toggleSubmitGroupLeaveSlip()}
          toggleOtherReasons={() => toggleOtherReasons()}
          otherReasonsShow={otherReasonsShow}
          selectedEvents={selectedEvents}
          tas={tas}
          initialValues={{informStatus: "true"}}
        />
      </div>
    </div>
  )
}

ActionBar.propTypes = {
  submitRollShow: PropTypes.bool.isRequired, 
  submitLeaveSlipShow: PropTypes.bool.isRequired, 
  submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  toggleSubmitRoll: PropTypes.func.isRequired, 
  toggleSubmitLeaveSlip: PropTypes.func.isRequired, 
  toggleSubmitGroupLeaveSlip: PropTypes.func.isRequired
}

export default ActionBar

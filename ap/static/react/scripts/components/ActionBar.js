import React, { PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SelectedEvent from './SelectedEvent'
import RollSlipForm from './RollSlipForm'
import GroupSlipForm from './GroupSlipForm'

const ActionBar = ({submitRollShow, submitLeaveSlipShow, submitGroupLeaveSlipShow, otherReasonsShow,
                    selectedEvents, formSuccess, trainee, traineeSelectOptions, isSecondYear, tas, lsdShow, gsdShow,
                    toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupSlip, toggleOtherReasons,
                    removeSelectedEvent, removeAllSelectedEvents, postRollSlip, postGroupSlip }) => {
  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }

  var hideRoll = {};
  if (trainee.terms_attended[trainee.terms_attended.length-1] <= 2) {
    hideRoll = {display: "none"};
  }

  return (
    <div style={{marginBottom: "10px"}}>
    {/*Form control buttons*/}
      <div>
        <Button className="action-button" onClick={toggleSubmitRoll} style={hideRoll} disabled={lsdShow}>Roll</Button>
        <Button className="action-button" onClick={toggleSubmitLeaveSlip}>Leave Slip</Button>
        <Button className="action-button" onClick={toggleSubmitGroupSlip}>Group Leave Slip</Button>
      </div>
    {/*Sessions selected*/}
      <div>
        <Collapse in={(selectedEvents.length > 0 || submitRollShow || submitLeaveSlipShow) && (!lsdShow && !gsdShow)}>
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
          selectedEvents={selectedEvents}
          isSecondYear={isSecondYear}
          isSlipDetail={false}
          lsdShow={lsdShow}
        />
      </div>
    {/*Group slip form*/}
      <div>
        <GroupSlipForm
          post={(groupSlip) => postGroupSlip(groupSlip, selectedEvents)}
          submitGroupLeaveSlipShow={submitGroupLeaveSlipShow}
          toggleSubmitGroupSlip={() => toggleSubmitGroupSlip()}
          toggleOtherReasons={() => toggleOtherReasons()}
          otherReasonsShow={otherReasonsShow}
          selectedEvents={selectedEvents}
          tas={tas}
          initialValues={{informed: "true"}}
          traineeSelectOptions={traineeSelectOptions}
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
  toggleSubmitGroupSlip: PropTypes.func.isRequired
}

export default ActionBar
